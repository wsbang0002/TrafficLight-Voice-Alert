
using System;
using System.IO;
using System.IO.Ports;
using System.Threading;

namespace TrafficLightSender
{
    class Program
    {
        static void Main()
        {
            // 파일 경로 (Python이 생성하는 신호 파일)
            string filePath = "signal_result.txt";

            // 시리얼 포트 설정 (필요시 COM 포트 번호 변경)
            string portName = "COM3";
            int baudRate = 9600;

            // 이전에 전송한 신호 저장 (중복 전송 방지용)
            string lastSignal = "";

            try
            {
                using (SerialPort port = new SerialPort(portName, baudRate))
                {
                    port.Open();
                    Console.WriteLine($"[INFO] 포트 {portName} 열림, Baud: {baudRate}");

                    while (true)
                    {
                        if (File.Exists(filePath))
                        {
                            string signal = File.ReadAllText(filePath).Trim().ToUpper();

                            if ((signal == "RED" || signal == "GREEN") && signal != lastSignal)
                            {
                                port.WriteLine(signal);
                                Console.WriteLine($"[SEND] 아두이노에 전송: {signal}");
                                lastSignal = signal;
                            }
                        }

                        Thread.Sleep(1000); // 1초마다 체크
                    }
                }
            }
            catch (IOException ex)
            {
                Console.WriteLine("[ERROR] 시리얼 포트 오류: " + ex.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("[ERROR] 일반 오류: " + ex.Message);
            }
        }
    }
}
