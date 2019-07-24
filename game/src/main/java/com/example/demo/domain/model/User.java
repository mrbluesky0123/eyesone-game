package com.example.demo.domain.model;

public class User {
	private String userName;
	private String sessionId;
	
	public User(String userName, String sessionId) {
		super();
		this.userName = userName;
		this.sessionId = sessionId;
	}
	
	public String getUserName() {
		return userName;
	}
	
	public void setUserName(String userName) {
		this.userName = userName;
	}
	
	public String getSessionId() {
		return sessionId;
	}
	
	public void setSessionId(String sessionId) {
		this.sessionId = sessionId;
	}
}
