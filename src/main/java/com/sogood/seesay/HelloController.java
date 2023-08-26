package com.sogood.seesay;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
public class HelloController {

    @CrossOrigin(origins = "*")
    @GetMapping("/")
    public Message index() throws InterruptedException, IOException {
        return new Message(0, "TEST");
//        ProcessBuilder processBuilder = new ProcessBuilder("python", "scripts/test.py");
//        processBuilder.redirectErrorStream(true);
//
//        Process process = processBuilder.start();
//        int exitCode = process.waitFor();
//
//        System.out.println(exitCode);
//
//        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
//        StringBuilder builder = new StringBuilder();
//        String line = null;
//        while ( (line = reader.readLine()) != null) {
//            builder.append(line);
//            builder.append(System.getProperty("line.separator"));
//        }
//        String result = builder.toString();
//        return new Message(0, result);
    }

}