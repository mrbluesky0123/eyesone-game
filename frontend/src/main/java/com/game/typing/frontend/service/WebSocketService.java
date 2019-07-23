package com.game.typing.frontend.service;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

@Service
public class WebSocketService {

	
	
    private static final SimpleDateFormat dateFormatter = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");

    @Autowired
    private SimpMessagingTemplate template;

    public void sendMessage(String topic, String message) {
        StringBuilder builder = new StringBuilder();
        builder.append("[");
        builder.append(dateFormatter.format(new Date()));
        builder.append("]");
        builder.append(message);

        this.template.convertAndSend("/topic/" + topic, builder.toString());

    }

	

}
