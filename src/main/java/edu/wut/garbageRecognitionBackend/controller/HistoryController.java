package edu.wut.garbageRecognitionBackend.controller;

import edu.wut.garbageRecognitionBackend.entity.History;
import edu.wut.garbageRecognitionBackend.service.HistoryService;
import edu.wut.garbageRecognitionBackend.utils.ResponseUtil;
import edu.wut.garbageRecognitionBackend.utils.TokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@CrossOrigin
public class HistoryController {

    @Autowired
    private HistoryService historyService;

    @Autowired
    private ResponseUtil<List<History>> getResponseUtil;

    @Autowired
    private ResponseUtil<String> postResponseUtil;

    @Autowired
    private TokenUtil tokenUtil;

    @GetMapping("/history")
    public ResponseUtil<List<History>> getHistory(String token) {
        String openid = tokenUtil.verifyToken(token);
        if (openid == null) {
            getResponseUtil.setCode(500);
            getResponseUtil.setObject(null);
        } else {
            List<History> histories = historyService.selectHistoryByOpenid(openid);
            getResponseUtil.setCode(0);
            getResponseUtil.setObject(histories);
        }

        return getResponseUtil;
    }

    @PostMapping("/history")
    public ResponseUtil<String> postHistory(String token, String imageURL, String result) {
        String openid = tokenUtil.verifyToken(token);
        if (openid == null) {
            postResponseUtil.setCode(500);
            postResponseUtil.setObject(null);
        } else {
            int i = historyService.insertHistorySelective(openid, imageURL, result);
            if (i > 0) {
                postResponseUtil.setCode(0);
                postResponseUtil.setObject("insert " + i + " records");
            }
        }

        return postResponseUtil;
    }
}
