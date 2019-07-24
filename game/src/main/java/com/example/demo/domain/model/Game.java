package com.example.demo.domain.model;

public class Game {
	private String content;
	private int level;
	private User user;
	
	public Game(String content, int level) {
		super();
		this.content = content;
		this.level = level;
	}

	public Game(String content, int level, User user) {
		super();
		this.content = content;
		this.level = level;
		this.user = user;
	}

	public Game() {
		super();
	}

	public String getContent() {
		return content;
	}
	
	public void setContent(String content) {
		this.content = content;
	}
	
	public int getLevel() {
		return level;
	}
	
	public void setLevel(int level) {
		this.level = level;
	}

	public User getUser() {
		return user;
	}

	public void setUser(User user) {
		this.user = user;
	}
	
}
