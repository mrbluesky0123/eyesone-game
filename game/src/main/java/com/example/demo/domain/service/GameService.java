package com.example.demo.domain.service;

import java.util.Map;

import com.example.demo.domain.model.Game;

public interface GameService {

	Game requestNextGame(String level);

	boolean checkAnswer(Map<String, String> map);

}
