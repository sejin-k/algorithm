using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class A_star : MonoBehaviour {

	public int[,] start_state;
	public int[,] goal_state;
	private List<Node> openlist;
	private List<Node> closelist;
	public List<int[,]> path;

	// Node 클래스 정의
	public class Node {
		public int[,] cur_state;
		public int f_val;
		public int g_val;
		public int h_val;
		public int[,] parent_state;

		public Node (int[,] cur, int f, int g, int h, int[,] parent){
			this.cur_state = cur;
			this.f_val = f;
			this.g_val = g;
			this.h_val = h;
			this.parent_state = parent;
		}
	}
	
	// test하기 위한 초기 설정
	public void set_initial(){
		int h_val;

		this.openlist = new List<Node>();
		this.closelist = new List<Node>();
		h_val = set_h_val(this.start_state);
		Node start = new Node(this.start_state, 0 + h_val, 0, h_val, null);
		this.openlist.Add(start);
	}

	// a* algorithm
	public void a_star_algorithm() {
		/*
		#################################### a* algoritm sequence ####################################
		1. openlist에서 f값이 가장 낮은 node(lowest)를 찾아서 선택
		2. lowest Node가 갈 수 있는 다음 state들 list에 저장(movable_nodes)
		3. movable_nodes의 각 Node들이 openlist에 있는 경우 
			-> 기존보다 f값이 작으면 교체, 크면 pass
		4. openlist에 없고 closelist에 있는 경우 
			-> 기존보다 f값이 작으면 closelist의 값 삭제후 새로운 node를 openlist에 추가, 없으면 pass
		5. openlist와 closelist에 없을 경우 openlist에 추가
		6. lowest node를 closelist에 추가
		7. lowest node의 state가 goal state와 같을때 까지 1~6번 과정 반복
		##############################################################################################
		*/
		bool hasNode = false;
		Node lowest = null;
		List<Node> movable_nodes = new List<Node>();

		for(int i = 0; i < 10000; i++) {
		// while(this.openlist.Count != 0){		// 악의 경우의 수 수행시간이 너무 길어서 오류 발생
			// openlist에서 f가 가장 작은값 찾기
			lowest = lowest_node();
			this.openlist.Remove(lowest);

			// 목적지에 도착할 경우 반복문 나가기
			if(isSameState(lowest.cur_state, this.goal_state)) {
				this.closelist.Add(lowest);
				break;
			}

			// lowest가 움직일 수 있는 다음 state들 list
			movable_nodes = find_next_state(lowest);

			// 다음 state들 검사
			foreach(Node n in movable_nodes) {
				foreach(Node o in this.openlist) {
					if(isSameState(n.cur_state, o.cur_state)) {
						hasNode = true;
						if(n.g_val < o.g_val) {
							this.openlist.Remove(o);
							this.openlist.Add(n);
							break;
						}
						else{
							break;
						}
					}
				}

				if(!hasNode) {
					foreach(Node c in this.closelist) {
						if(isSameState(n.cur_state, c.cur_state)) {
							hasNode = true;
							if(n.g_val < c.g_val) {
								this.closelist.Remove(c);
								this.openlist.Add(n);
								break;
							}
							else {
								break;
							}
						}
					}
				}

				if(!hasNode) {
					this.openlist.Add(n);
				}
				hasNode = false;
			}

			this.closelist.Add(lowest);
		}

		if(!isSameState(lowest.cur_state, this.goal_state)){
			Debug.Log("Error : Don't arrive goal state, openlist is empty");
		}
	}

	// heuristic 값을 구하는 함수1 (miss match인 노드들의 개수)
	public int set_h_val (int[,] cur_state) {
		int val = 0;

		for (int i=0; i < cur_state.GetLength(0); i++) {
			for (int j=0; j < cur_state.GetLength(1); j++) {
				if(cur_state[i,j] != this.goal_state[i,j]){
					val++;
				}
			}
		}

		return val;
	}

	// heuristic 값을 구하는 함수2 (각 노드들의 다른 위치의 정도의 합)
	public int set_h_val2 (int[,] cur_state) {
		int val = 0;
		bool exit = false;

		for (int i=0; i < cur_state.GetLength(0); i++) {
			for (int j=0; j < cur_state.GetLength(1); j++) {
				for(int h=0; h < this.goal_state.GetLength(0); h++) {
					for(int w=0; w < this.goal_state.GetLength(1); w++) {
						if(cur_state[i,j] == goal_state[h,w]) {
							val += Mathf.Abs(h-i)+Mathf.Abs(w-j);
							exit = true;
							break;
						}
					}
					if (exit == true){
						exit = false;
						break;
					}
				}
				
			}
		}

		return val;
	}
	
	// openlist에서 f값이 가장 낮은 Node 구하기
	public Node lowest_node() {
		Node lowest = null;

		foreach(Node n in this.openlist) {
			if(lowest != null) {
				if (lowest.f_val > n.f_val) {
					lowest = n;
				}
			}
			else {
				lowest = n;
			}
		}

		return lowest;
	}

	// Find blank(-1)'s position (x,y)
	public int[] find_blank_pos(int[,] state) {
		int[] res = new int[2];

		for (int i=0; i < state.GetLength(0); i++){
			for (int j=0; j < state.GetLength(1); j++){
				if (state[i,j] == -1){
					res[0] = j;
					res[1] = i;
					return res;		// return blank's (x,y) position
				}
			}
		}

		return res;
	}

	// 움직일 수 있는 다음 state를 구하는 함수
	public List<Node> find_next_state (Node node) {
		List<Node> res = new List<Node>();
		int[] cur_position;
		int[,] new_state;
		int new_hVal, new_gVal;
		int temp;
		
		cur_position = find_blank_pos(node.cur_state);

		// 오른쪽으로 갈 수 있는 경우
		if (cur_position[0]+1 < 3) {
			new_state = (int[,])node.cur_state.Clone();
			temp = new_state[cur_position[1], cur_position[0] + 1];
			new_state[cur_position[1], cur_position[0]] = temp;
			new_state[cur_position[1], cur_position[0] + 1] = -1;
			new_gVal = node.g_val + 1;
			new_hVal = set_h_val(new_state);
			res.Add(new Node(new_state, new_gVal + new_hVal, new_gVal, new_hVal, node.cur_state));
		}
		// 왼쪽으로 갈 수 있는 경우
		if (cur_position[0]-1 > -1) {
			new_state = (int[,])node.cur_state.Clone();
			temp = new_state[cur_position[1], cur_position[0] - 1];
			new_state[cur_position[1], cur_position[0]] = temp;
			new_state[cur_position[1], cur_position[0] - 1] = -1;
			new_gVal = node.g_val + 1;
			new_hVal = set_h_val(new_state);
			res.Add(new Node(new_state, new_gVal + new_hVal, new_gVal, new_hVal, node.cur_state));
		}
		// 위쪽으로 갈 수 있는 경우
		if (cur_position[1]-1 > -1) {
			new_state = (int[,])node.cur_state.Clone();
			temp = new_state[cur_position[1] - 1, cur_position[0]];
			new_state[cur_position[1], cur_position[0]] = temp;
			new_state[cur_position[1] - 1, cur_position[0]] = -1;
			new_gVal = node.g_val + 1;
			new_hVal = set_h_val(new_state);
			res.Add(new Node(new_state, new_gVal + new_hVal, new_gVal, new_hVal, node.cur_state));
		}
		// 아래쪽으로 갈 수 있는 경우
		if (cur_position[1]+1 < 3) {
			new_state = (int[,])node.cur_state.Clone();
			temp = new_state[cur_position[1] + 1, cur_position[0]];
			new_state[cur_position[1], cur_position[0]] = temp;
			new_state[cur_position[1] + 1, cur_position[0]] = -1;
			new_gVal = node.g_val+1;
			new_hVal = set_h_val(new_state);
			res.Add(new Node(new_state, new_gVal+new_hVal, new_gVal, new_hVal, node.cur_state));
		}

		return res;
	}

	// 최종 길찾기
	public void final_path() {
		List<Node> tempClose = this.closelist.ConvertAll(n => new Node(n.cur_state, n.f_val, n.g_val, n.h_val, n.parent_state));
		this.path = new List<int[,]>();
		Node cur_node;
		int[,] current;

		if (isSameState(tempClose[tempClose.Count - 1].cur_state, this.goal_state)) {
			cur_node = tempClose[tempClose.Count - 1];
			this.path.Add(cur_node.cur_state);
			current = cur_node.parent_state;
			while(!isSameState(this.start_state, current)){
				foreach(Node n in tempClose) {
					if(isSameState(current, n.cur_state)){
						this.path.Add(current);
						current = n.parent_state;
						tempClose.Remove(n);
						break;
					}
				}
			}
			if(isSameState(this.start_state, current)){
				this.path.Add(current);
			}
		} 
		else {
			Debug.Log("Didn't arrive goal_state");
		}
		this.path.Reverse();
	}

	// 두 2차원 배열이 같은지 비교하는 함수.
	public bool isSameState(int[,] state_1, int[,] state_2){
		for (int h = 0; h < state_1.GetLength(0); h++){
			for(int w = 0; w < state_1.GetLength(1); w++){
				if (state_1[h,w] != state_2[h,w]){
					return false;
				}
			}
		}

		return true;
	}
	
	// state 배열을 출력 디버깅 하기 위함
	public void print_state(int[,] s){
		string str = "\n  ";

		for (int h=0; h<s.GetLength(0); h++){
			for(int w=0; w<s.GetLength(1); w++){
				str += s[h,w] + " ";
			}
			str += "\n  ";
		}
		Debug.Log(str);
	}

	public void main() {
		set_initial();
		a_star_algorithm();
		final_path();
	}
}