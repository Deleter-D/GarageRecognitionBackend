package edu.wut.garagerecognitionbackend;

import edu.wut.garbageRecognitionBackend.utils.TokenUtil;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = {GarageRecognitionBackendApplicationTests.class})
public class TokenTest {


    @Test
    public void tokenTest() {
        TokenUtil tokenUtil = new TokenUtil();
        String token = tokenUtil.createToken("123");
        System.out.println(token);

        String openid = tokenUtil.verifyToken(token + "2");
        System.out.println(openid);
    }
}
