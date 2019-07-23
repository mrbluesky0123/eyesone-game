package com.game.typing.communication;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.game.typing.communication.service.CommunicationService;

@RestController
@RequestMapping("/v1/communication")
public class CommunicationController {

	
	@Autowired
	private CommunicationService communicationService;
	
	@PostMapping
	public String postMessage(@RequestBody String message) {
		try {
			communicationService.sendMessage(message);
			return "ok";
		}catch (Exception e) {
			throw e;
		}
	}
}
