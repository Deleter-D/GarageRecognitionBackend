package edu.wut.garbageRecognitionBackend.utils;

import lombok.Data;
import org.springframework.stereotype.Component;

@Data
@Component
public class ResponseUtil<T> {

    private int code;
    private T object;
}
