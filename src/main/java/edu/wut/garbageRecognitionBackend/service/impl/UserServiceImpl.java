package edu.wut.garbageRecognitionBackend.service.impl;

import edu.wut.garbageRecognitionBackend.entity.User;
import edu.wut.garbageRecognitionBackend.mapper.UserMapper;
import edu.wut.garbageRecognitionBackend.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper userMapper;

    @Override
    public int binding(String openid) {
        User user = new User();
        user.setOpenid(openid);

        return userMapper.insert(user);
    }
}
