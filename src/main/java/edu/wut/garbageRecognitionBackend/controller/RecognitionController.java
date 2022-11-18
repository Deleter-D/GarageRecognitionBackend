package edu.wut.garbageRecognitionBackend.controller;

import edu.wut.garbageRecognitionBackend.utils.ResponseUtil;
import edu.wut.garbageRecognitionBackend.utils.SocketClientUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin
public class RecognitionController {

    @Autowired
    private SocketClientUtil socketClientUtil;

    @Autowired
    private ResponseUtil<String> responseUtil;

    @GetMapping("/recognition")
    public ResponseUtil<String> recognition(String imageURL) {
        String url = imageURL.substring(imageURL.lastIndexOf("/") + 1);
        String result = socketClientUtil.sendImageURLToPython(url);
        if (result != null && !result.equals("")) {
            responseUtil.setCode(0);
            responseUtil.setObject(result);
        } else {
            responseUtil.setCode(500);
            responseUtil.setObject(null);
        }

        return responseUtil;
    }
}
