package com.sogood.seesay;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

@SpringBootApplication
public class SeesayApplication {

	public static void main(String[] args) {
		SpringApplication.run(SeesayApplication.class, args);
	}

//	@Bean
//	public CommandLineRunner commandLineRunner(ApplicationContext ctx){
//		return args -> {
//
////			ProcessBuilder processBuilder = new ProcessBuilder("python", "./src/main/resources/scripts/test.py");
////			processBuilder.redirectErrorStream(true);
////
////			Process process = processBuilder.start();
////			int exitCode = process.waitFor();
////
////			System.out.println(exitCode);
////
////			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
////			StringBuilder builder = new StringBuilder();
////			String line = null;
////			while ( (line = reader.readLine()) != null) {
////				builder.append(line);
////				builder.append(System.getProperty("line.separator"));
////			}
////			String result = builder.toString();
////			System.out.println(result);
//
////			System.out.println("Let's inspect the beans provided by Spring Boot:");
////
////			String[] beanNames = ctx.getBeanDefinitionNames();
////			Arrays.sort(beanNames);
////			for (String beanName : beanNames) {
////				System.out.println(beanName);
////			}
//		};
//	}

}
