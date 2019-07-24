package com.sns.app.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class SnsController {
	
//	@Autowired
//	SnsService snsService;
	
	@RequestMapping(value = "/snsLink")
	public String main() {
		
		System.out.println("===========snsLink=============in");
		
		return "/main/snsLink";
	}
	
	
	
}
