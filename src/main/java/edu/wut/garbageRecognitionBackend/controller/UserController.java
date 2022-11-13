package edu.wut.garbageRecognitionBackend.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class UserController {

    @PostMapping("/binding")
    public void bindUser(String code) {

    }
}
