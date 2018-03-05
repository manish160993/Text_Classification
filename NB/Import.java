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
	
	int importNoOfDocs(String s){
		File folder = new File(s);
		File[] listOfFiles = folder.listFiles();
		return listOfFiles.length;
	}
	
		
	HashMap<String,Double> calculateConditional(HashSet<String> vocab,HashMap<String,Integer> k){
		HashMap<String,Double> h=new HashMap<String,Double>();
		int total=0;
		Iterator<String> it = vocab.iterator();
		while(it.hasNext()){
			String s=it.next();
			h.put(s,(double)k.getOrDefault(s,0));
			total+=h.get(s);
		}
		for (Map.Entry<String, Double> entry : h.entrySet()) {
				h.put(entry.getKey(),(entry.getValue()+1)/(total+vocab.size()));
		}
		return h;
	}
	
	HashSet<String> importWords(HashMap<String,Integer> h,HashSet<String> s){
		for (Map.Entry<String, Integer> entry : h.entrySet()) {
				s.add(entry.getKey());
		}
		return s;
	}
}