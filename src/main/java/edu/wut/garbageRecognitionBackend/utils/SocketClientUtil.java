package edu.wut.garbageRecognitionBackend.utils;

import org.springframework.stereotype.Component;

import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

@Component
public class SocketClientUtil {

    public String sendImageURLToPython(String imageURL) {

        InetAddress host = null;
        try {
            host = InetAddress.getLocalHost();
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        }

        try (
                // 初始化Socket
                Socket socket = new Socket(host.getHostAddress(), 10000);
        ) {

            // 获取输出流
            OutputStream outputStream = socket.getOutputStream();
//            PrintStream printStream = new PrintStream(outputStream);
            BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(outputStream));
            // 写入内容
            bufferedWriter.write(imageURL);
            bufferedWriter.write("over");
            bufferedWriter.flush();

            // 获取ServerSocket输入流
            InputStream inputStream = socket.getInputStream();
            // 将输入流利用InputStreamReader读入BufferedReader
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream, "utf-8"));
            StringBuilder stringBuilder = new StringBuilder();
            String temp = null;
            // 利用BufferedReader和StringBuilder构建结果
            while ((temp = bufferedReader.readLine()) != null)
                stringBuilder.append(temp);

            return stringBuilder.toString();
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
