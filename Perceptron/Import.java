import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.*;
import java.util.*;

class Import{
	HashMap<String,Integer> importWordCount(String s1){
		HashMap<String,Integer> h=new HashMap<String,Integer>();
		try{
		File folder = new File(s1);
		File[] listOfFiles = folder.listFiles();

		for (File file : listOfFiles) {
			if (file.isFile()) {
			//System.out.println(file.getName());
			
 
		BufferedReader br = new BufferedReader(new FileReader(file));
 
		String st;
		while ((st = br.readLine()) != null)
		{
			String[] s=st.split(" ");
			for(int i=0;i<s.length;i++)
				h.put(s[i],h.getOrDefault(s[i],0)+1);
		}
		}
		}
		}
		catch(Exception e){
			System.out.println(e);
		}
		return h;
	}
	
	HashMap<String,Integer> importWords(HashMap<String,Integer> h,HashMap<String,Integer> s){
		for (Map.Entry<String, Integer> entry : h.entrySet()) {
				s.put(entry.getKey(),0);
		}
		return s;
	}
}