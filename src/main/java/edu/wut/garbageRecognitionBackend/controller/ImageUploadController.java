package edu.wut.garbageRecognitionBackend.controller;

import edu.wut.garbageRecognitionBackend.service.ImageService;
import edu.wut.garbageRecognitionBackend.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;
import java.util.UUID;

@RestController
@CrossOrigin
public class ImageUploadController {

    @Autowired
    private ResponseUtil<String> responseUtil;

    @Autowired
    private ImageService imageService;


    @PostMapping("/upload_image")
    public ResponseUtil<String> uploadImage(@RequestParam("image") MultipartFile image, HttpServletRequest request) {
        if (image.isEmpty()) {
            responseUtil.setCode(500);
            responseUtil.setObject(null);
        } else {
            String imageURL = imageService.uploadImage(image, request);
            if (imageURL != null) {
                responseUtil.setCode(0);
                responseUtil.setObject(imageURL);
            } else {
                responseUtil.setCode(500);
                responseUtil.setObject(null);
            }
        }
        return responseUtil;
    }
}
