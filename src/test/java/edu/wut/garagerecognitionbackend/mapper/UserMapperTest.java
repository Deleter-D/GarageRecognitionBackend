package edu.wut.garagerecognitionbackend.mapper;

import edu.wut.garbageRecognitionBackend.GarageRecognitionBackendApplication;
import edu.wut.garbageRecognitionBackend.entity.User;
import edu.wut.garbageRecognitionBackend.mapper.UserMapper;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = {GarageRecognitionBackendApplication.class})
public class UserMapperTest {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void insertTest() {
        User user = new User();
        user.setOpenid("123");
        userMapper.insertSelective(user);
    }

    @Test
    public void selectTest() {
        System.out.println(userMapper.selectByPrimaryKey(1));
    }

}
