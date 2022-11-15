package edu.wut.garbageRecognitionBackend.service.impl;

import edu.wut.garbageRecognitionBackend.entity.History;
import edu.wut.garbageRecognitionBackend.mapper.HistoryMapper;
import edu.wut.garbageRecognitionBackend.service.HistoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class HistoryServiceImpl implements HistoryService {

    @Autowired
    private HistoryMapper historyMapper;

    @Override
    public List<History> selectHistoryByOpenid(String openid) {

        return historyMapper.selectByOpenid(openid);
    }

    @Override
    public int insertHistorySelective(String openid, String imageURL, String result) {
        History history = new History();
        history.setOpenid(openid);
        history.setImageUrl(imageURL);
        history.setResult(result);

        return historyMapper.insertSelective(history);
    }
}
