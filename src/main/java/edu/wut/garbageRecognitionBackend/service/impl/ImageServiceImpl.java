package edu.wut.garbageRecognitionBackend.service.impl;

import edu.wut.garbageRecognitionBackend.service.ImageService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;
import java.util.UUID;

@Service
public class ImageServiceImpl implements ImageService {

    @Value("${upload-path}")
    private String imagePath;

    @Override
    public String uploadImage(MultipartFile image, HttpServletRequest request) {

        // 若不存在存储文件的文件夹，则创建
        File imageDirectory = new File(imagePath);
        if (!imageDirectory.exists())
            imageDirectory.mkdir();

        // 获取图片名，并提取图片格式
        String imageName = image.getOriginalFilename();
        int lastIndexOf = imageName.lastIndexOf(".");
        String imageFormat = imageName.substring(lastIndexOf + 1);

        // 生成图片的UUID，防止重名
        String imageUUID = UUID.randomUUID().toString().replace("-", "");
        // 为即将存储下来的图片命名
        File localImage = new File(imagePath + imageUUID + "." + imageFormat);


        try {
            image.transferTo(localImage);
            // 生成前端访问图片的URL
            String imageURL = request.getScheme() + "://"
                    + request.getServerName() + ":"
                    + request.getServerPort()
                    + "/images/" + imageUUID + "." + imageFormat;

            return imageURL;
        } catch (IOException e) {
            return null;
        }
    }
}
