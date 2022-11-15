package edu.wut.garbageRecognitionBackend.service;

import edu.wut.garbageRecognitionBackend.entity.History;

import java.util.List;

public interface HistoryService {

    public List<History> selectHistoryByOpenid(String openid);

    public int insertHistorySelective(String openid, String imageURL, String result);
}
