package com.example.demo.domain.service;

import java.util.List;

import com.example.demo.domain.model.Game;

public interface GameService {
	
	Game findByUserName(String userName);
	
	List<Game> findAll();
	
	String GetNextGame(String level);
}
