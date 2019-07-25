package com.game.typing.frontend.controller;

import java.util.Map;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.bind.annotation.CrossOrigin;

import com.game.typing.frontend.service.WebSocketService;

@CrossOrigin(origins="*")
@Controller
@SessionAttributes("sessionId")
public class FrontController{

	@Autowired
	private WebSocketService webSocketService;
	
	@GetMapping("/")
	public String indexPage() {
		return "index";
	}
	
	@GetMapping("/main/{sessionId}/{userName}")
	public ModelAndView mainPage(ModelMap model, @PathVariable("sessionId") String sessionId, @PathVariable("userName") String userName) {
		
		System.out.println("=====main controller=====");
		
		System.out.println("sessionId===>"+sessionId);
		System.out.println("userName===>"+userName);
		
//		System.out.println("res===>"+ response.);
		//test data
		model.put("sessionId", sessionId);
		model.put("userName", userName);
		model.put("level", "1");
		
						
		return new ModelAndView("main",model);
	}
	
	
	@GetMapping("/result/{sessionId}/{userName}/{level}/{clearTime}")
	public ModelAndView resultPage(ModelMap model, @PathVariable("sessionId") String sessionId, @PathVariable("userName") String userName, @PathVariable("level") int level, @PathVariable("clearTime") int clearTime ) {
		System.out.println("=======result controller=====");
		
		model.put("sessionId", sessionId);
		model.put("userName", userName);
		model.put("level", level);
		model.put("clearTime", clearTime);		
		
		return new ModelAndView("result", model);
	}
	
	
	@PostMapping("/popup")
	public String test(@RequestBody String message) {
		webSocketService.sendMessage("browser", message);
		
		String test = "success";
		return test;
		
	}
	
	

}
