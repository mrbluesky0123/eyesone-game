package com.example.demo.domain.model;

public class Game {
	private String contents;
	private int level;
	private User user;
	
	public Game(String contents, int level) {
		super();
		this.contents = contents;
		this.level = level;
	}

	public Game(String contents, int level, User user) {
		super();
		this.contents = contents;
		this.level = level;
		this.user = user;
	}

	public Game() {
		super();
	}

	public String getContents() {
		return contents;
	}
	
	public void setContents(String contents) {
		this.contents = contents;
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
