package com.game.typing.frontend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.game.typing.frontend.service.WebSocketService;

@Controller
public class FrontController {

	@Autowired
	private WebSocketService webSocketService;
	
	@GetMapping("/")
	public String fstPage() {
		return "index";
	}
	
	@PostMapping("/popup")
	public String test(@RequestBody String message) {
		webSocketService.sendMessage("browser", message);
		
		String test = "success";
		return test;
		
	}
}
