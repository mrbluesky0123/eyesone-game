package com.example.demo.domain.service;

import java.util.Map;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.example.demo.domain.model.Game;

@Service("gameLogic")
public class GameLogic implements GameService {

	@Transactional(readOnly=true)
	public String geneateContent(String level) {
		// TODO Auto-generated method stub
		String content = "";
		
	    for (int i = 1; i <= Integer.valueOf(level); i++) {
	    	char ch = (char) ((Math.random() * 11172) + 0xAC00) ;
	    	content += String.valueOf(ch);
	    }
		
		return content;
	}
	
	@Override
	public Game requestNextGame(String level) {
		// TODO Auto-generated method stub
		Game game = new Game();

		game.setContent(geneateContent(level));
		game.setLevel(Integer.valueOf(level));

		return game;
	}

	@Override
	public boolean checkAnswer(Map<String, String> map) {
		// TODO Auto-generated method stub
		if( map.get("content").equals(map.get("answer")) )
			return true;
		
		return false;
	}
}
