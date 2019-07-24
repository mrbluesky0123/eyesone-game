package com.example.demo.application.sp.web;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.domain.model.Game;
import com.example.demo.domain.service.GameService;

@RestController
@RequestMapping("/games")
public class GameRestController implements GameService {
	@Autowired
	private GameService gameService;

	@Override
	public Game findByUserName(String userName) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public List<Game> findAll() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	@GetMapping("/{level}")
	public String GetNextGame(@PathVariable("level") String level) {
		// TODO Auto-generated method stub
		String contents = gameService.GetNextGame(level);
		return contents;
	}
}
