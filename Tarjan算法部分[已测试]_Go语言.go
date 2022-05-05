package main

import "sort"

//tarjan algorithm
func dfs(acc *account, stack *[]*account, time int, m *map[int]*account, visited *map[int]bool, Sccs *[][]*account, nodes *[]*node) int {
	if acc.onStack {
		return acc.j
	}
	acc.i, acc.j = time, time
	acc.onStack = true
	*stack = append(*stack, acc)
	for i := 0; i < len(acc.next); i++ {
		if (*visited)[acc.next[i].ID] == false {
			acc.j = min(acc.j, dfs(acc.next[i], stack, time+1, m, visited, Sccs, nodes))
		}
	}
	if acc.i == acc.j {
		var temp []*account //单个SCC
		for len(*stack) > 0 {
			popNode := (*stack)[len(*stack)-1]
			if popNode.j != acc.j {
				break
			}
			*stack = (*stack)[:len(*stack)-1]
			popNode.onStack = false
			(*visited)[popNode.ID] = true
			newnode := &node{ID: popNode.ID, refer: len(*Sccs)}
			*nodes = append(*nodes, newnode)
			temp = append(temp, popNode)
			delete(*m, popNode.ID)
		}
		if len(temp) > 0 {
			sort.Slice(temp, func(i, j int) bool {
				return temp[i].ID < temp[j].ID
			})
			*Sccs = append(*Sccs, temp)
		}
	}
	return acc.j
}

//注册建立每行两个ID之间的连接，节点不存在就创建
func register(id1, id2 int, m *map[int]*account) {
	if _, ok := (*m)[id1]; !ok {
		(*m)[id1] = &account{ID: id1}
	}
	if _, ok := (*m)[id2]; !ok {
		(*m)[id2] = &account{ID: id2}
	}
	(*m)[id1].next = append((*m)[id1].next, (*m)[id2])
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
