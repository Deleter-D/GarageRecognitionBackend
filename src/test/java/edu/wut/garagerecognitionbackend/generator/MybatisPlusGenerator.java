package edu.wut.garagerecognitionbackend.generator;

import com.baomidou.mybatisplus.generator.FastAutoGenerator;
import com.baomidou.mybatisplus.generator.config.OutputFile;
import com.baomidou.mybatisplus.generator.engine.FreemarkerTemplateEngine;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Collections;

@SpringBootTest
public class MybatisPlusGenerator {

    private static String projectDir = "D:\\StudyAndWork\\GitRepository\\GarageRecognitionBackend";

    public static void main(String[] args) {
        FastAutoGenerator.create("jdbc:mysql://127.0.0.1:3306/garbage_recognition?serverTimezone=UTC", "root", "wyp2000722")
                .globalConfig(builder -> {
                    builder.author("GoldPancake")
                            .enableSwagger()
                            .outputDir(projectDir + "\\src\\main\\java");
                })
                .packageConfig(builder -> {
                    builder.parent("edu.wut.garbageRecognitionBackend")
                            .pathInfo(Collections.singletonMap(OutputFile.xml, projectDir + "\\src\\main\\resources\\mapper"));
                })
                .strategyConfig(builder -> {
                    builder.addInclude("user")
                            .addInclude("history");
                })
                .templateEngine(new FreemarkerTemplateEngine())
                .execute();
    }
}
