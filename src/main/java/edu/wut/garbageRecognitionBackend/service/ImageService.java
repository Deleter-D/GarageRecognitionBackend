package edu.wut.garbageRecognitionBackend.service;


import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;

public interface ImageService {

    public String uploadImage(MultipartFile image, HttpServletRequest request);
}
