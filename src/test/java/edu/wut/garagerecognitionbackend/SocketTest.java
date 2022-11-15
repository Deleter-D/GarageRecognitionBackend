package edu.wut.garagerecognitionbackend;

import edu.wut.garbageRecognitionBackend.GarageRecognitionBackendApplication;
import edu.wut.garbageRecognitionBackend.utils.SocketClientUtil;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = {GarageRecognitionBackendApplication.class})
public class SocketTest {

    @Autowired
    private SocketClientUtil socketClientUtil;

    @Test
    public void SocketTest() {
        System.out.println(socketClientUtil.sendImageURLToPython("D:\\StudyAndWork\\GitRepository\\RecognitionModel\\test2.jpg"));
    }
}
