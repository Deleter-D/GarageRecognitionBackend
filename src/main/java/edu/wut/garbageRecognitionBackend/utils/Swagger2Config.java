package edu.wut.garbageRecognitionBackend.utils;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@Configuration
@EnableSwagger2
public class Swagger2Config {

    // configure the bean of the Docket of Swagger
    @Bean
    public Docket coreApiConfig() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(backendApiInfo())
                .groupName("backend")
                .select()
                .apis(RequestHandlerSelectors.basePackage("edu.wut.garbageRecognitionBackend.controller"))
                .build();
    }

    private ApiInfo backendApiInfo() {
        return new ApiInfoBuilder()
                .title("垃圾识别小程序——API文档")
                .description("垃圾识别小程序后端RESTFul API文档")
                .version("1.0")
                .contact(new Contact("GoldPancake", "https://deleter-d.github.io/", "867909454@qq.com"))
                .build();
    }
}
