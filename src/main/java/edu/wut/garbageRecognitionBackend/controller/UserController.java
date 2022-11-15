package edu.wut.garbageRecognitionBackend.controller;

import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONObject;
import com.fasterxml.jackson.databind.util.JSONPObject;
import edu.wut.garbageRecognitionBackend.entity.User;
import edu.wut.garbageRecognitionBackend.service.UserService;
import edu.wut.garbageRecognitionBackend.utils.ResponseUtil;
import edu.wut.garbageRecognitionBackend.utils.TokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@CrossOrigin
public class UserController {

    @Autowired
    private Environment environment;

    @Autowired
    private ResponseUtil<String> response;

    @Autowired
    private TokenUtil tokenUtil;

    @Autowired
    private UserService userService;

    @PostMapping("/binding")
    public ResponseUtil<String> bindUser(String code) {

        // 获取配置文件中的信息，拼接请求url
        String appid = environment.getProperty("miniApp.appid");
        String secret = environment.getProperty("miniApp.secret");
        String url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + appid + "&secret=" + secret + "&js_code=" + code + "&grant_type=authorization_code";

        // 发送请求，结果注入一个String中
        RestTemplate restTemplate = new RestTemplate();
        String resultStr = restTemplate.getForEntity(url, String.class).getBody();

        // 将String转换为JSON
        JSONObject resultJson = JSON.parseObject(resultStr);

        try {
            // 尝试获取openid
            String openid = resultJson.get("openid").toString();
            int isSuccess = userService.binding(openid);

            if (isSuccess != 0) {
                // 创建token并返回
                response.setCode(0);
                response.setObject(tokenUtil.createToken(openid));
                return response;
            } else {
                response.setCode(500);
                response.setObject(null);
                return response;
            }
        } catch (NullPointerException e) {
            response.setCode(500);
            response.setObject(null);
            return response;
        }
    }
}
