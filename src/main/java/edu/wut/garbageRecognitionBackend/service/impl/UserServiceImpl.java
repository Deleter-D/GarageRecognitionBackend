package edu.wut.garbageRecognitionBackend.service.impl;

import edu.wut.garbageRecognitionBackend.entity.User;
import edu.wut.garbageRecognitionBackend.mapper.UserMapper;
import edu.wut.garbageRecognitionBackend.service.IUserService;
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
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements IUserService {

}
