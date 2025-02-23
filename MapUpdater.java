import java.util.*;

public class MapUpdater{
	
	private static final int MAP_WIDTH = 10;
	private static final int MAP_HEIGHT = 10;
	private static char[][]map = new char[MAP_WIDTH][MAP_HEIGHT];
	
	public static void main(String[]args) throws InterruptedException{
		initializeMap();
		while(true){
			printMap();
			updateMap();
			Thread.sleep(4000);
		}
		
	}
	
	public static void initializeMap(){
		for(int i = 0; i < MAP_WIDTH; i++){
			for(int j = 0; j < MAP_HEIGHT; j++){
				map[i][j] = '·';
			}
		}
		map[5][5] = 'X'; //Initial position
	}
	
	public static void updateMap(){
		
		int x = (int)(Math.random() * MAP_WIDTH);
		int y = (int)(Math.random() * MAP_HEIGHT);
		map[x][y] = 'X';
	}
	
	public static void printMap(){
		//Clear the screen
		System.out.printf("\033[H \033[2J"); // Use of ANSI code. Works correctly in Linux, not in Windows
		System.out.flush();
		
		for(int i = 0; i < MAP_WIDTH; i++){
			for(int j = 0; j < MAP_HEIGHT; j++){
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
		
	}
	
	
}
