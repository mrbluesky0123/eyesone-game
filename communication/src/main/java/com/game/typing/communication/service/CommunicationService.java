package com.game.typing.communication.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

@Service
public class CommunicationService {
	
	private String message;
	
	private String userName;
	
	private String sessionId;
    @Autowired
    RestTemplate restTemplate;

	
	public void sendMessage(String _message) {
		String obj = restTemplate.postForObject("http://localhost:8081/popup", _message, String.class);
	}
	
	
}
