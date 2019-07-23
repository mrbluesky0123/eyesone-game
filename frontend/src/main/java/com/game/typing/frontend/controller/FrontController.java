package com.game.typing.frontend.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.game.typing.frontend.service.WebSocketService;

@Controller
public class FrontController{

	@Autowired
	private WebSocketService webSocketService;
	
	@GetMapping("/")
	public String indexPage() {
		return "index";
	}
	
	@GetMapping("/main")
	public String mainPage() {
		return "main";
	}
	
	@PostMapping("/enter")
	public String setUser(@RequestBody Map<String, String> body) {
		System.out.println(body.toString());
		System.out.println("hihi");
		return "main";
		
	}
	
	@PostMapping("/popup")
	public String test(@RequestBody String message) {
		webSocketService.sendMessage("browser", message);
		
		String test = "success";
		return test;
		
	}
	
	

}
