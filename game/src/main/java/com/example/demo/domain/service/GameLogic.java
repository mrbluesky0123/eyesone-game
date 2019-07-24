package com.example.demo.domain.service;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.example.demo.domain.model.Game;

@Service("gameLogic")
public class GameLogic implements GameService {

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
	@Transactional(readOnly=true)
	public String GetNextGame(String level) {
		// TODO Auto-generated method stub
		String contents = "";
		
	    for (int i = 1; i <= Integer.valueOf(level); i++) {
	    	char ch = (char) ((Math.random() * 11172) + 0xAC00) ;
	    	contents += String.valueOf(ch);
	    }
		
		return contents;
	}
}
