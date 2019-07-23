package com.sns.app.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class SnsController {
	
//	@Autowired
//	SnsService snsService;
	
	@RequestMapping(value = "/main")
	public String main() {
		
		System.out.println("들어오나 ???");
		
		return "/main/snsLink";
	}
	
}
