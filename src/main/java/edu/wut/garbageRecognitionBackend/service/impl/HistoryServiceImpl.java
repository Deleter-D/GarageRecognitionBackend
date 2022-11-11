package edu.wut.garbageRecognitionBackend.service.impl;

import edu.wut.garbageRecognitionBackend.entity.History;
import edu.wut.garbageRecognitionBackend.mapper.HistoryMapper;
import edu.wut.garbageRecognitionBackend.service.IHistoryService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author GoldPancake
 * @since 2022-11-11
 */
@Service
public class HistoryServiceImpl extends ServiceImpl<HistoryMapper, History> implements IHistoryService {

}
