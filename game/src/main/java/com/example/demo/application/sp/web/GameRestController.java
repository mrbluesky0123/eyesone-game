package com.example.demo.application.sp.web;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.domain.model.Game;
import com.example.demo.domain.service.GameService;

@RestController
@RequestMapping("/game")
public class GameRestController implements GameService {
	@Autowired
	private GameService gameService;

	@Override
	@GetMapping("/getQuestion/{level}")
	public Game requestNextGame(@PathVariable("level") String level) {
		// TODO Auto-generated method stub
		System.out.println("getQuestion");
		return  gameService.requestNextGame(level);
	}

	@Override
	@PostMapping("/checkAnswer")
	public boolean checkAnswer(@RequestBody Map<String, String> map) {
		// TODO Auto-generated method stub
		System.out.println("checkAnswer");
		System.out.println(map);
		return gameService.checkAnswer(map);
	}
}
