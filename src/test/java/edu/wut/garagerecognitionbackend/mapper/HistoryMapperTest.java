package edu.wut.garagerecognitionbackend.mapper;

import edu.wut.garbageRecognitionBackend.GarageRecognitionBackendApplication;
import edu.wut.garbageRecognitionBackend.entity.History;
import edu.wut.garbageRecognitionBackend.mapper.HistoryMapper;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.List;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = {GarageRecognitionBackendApplication.class})
public class HistoryMapperTest {

    @Autowired
    private HistoryMapper historyMapper;

    @Test
    public void getHistoryByOpenidTest() {
        List<History> list = historyMapper.selectByOpenid("on7s35NZOWW2SkyllnvBicasblHM");
        for (History history : list)
            System.out.println(history);
    }
}
