function biggestSubGraph(graph, node) {
  let result = [];
  arrMap = {};
  for (let i = 0; i < graph.length; i++) {
    if (!arrMap[graph[i][0]]) arrMap[graph[i][0]] = [];
    arrMap[graph[i][0]].push(graph[i][1]);
  }
  travel(arrMap, node, result, node);
  return result;
}

function travel(arrMap, node, result, start) {
  if (!arrMap[node]) {
    return false;
  } else {
    for (let i = 0; i < arrMap[node].length; i++) {
      if (node == start) {
        result[result.length] = [];
      }
      result[result.length - 1].push([node, arrMap[node][i]]);
      travel(arrMap, arrMap[node][i], result, start);
    }
  }
}

graphs = [];
nodes = [];
nodes[0] = "D";
graphs[0] = [];
graphs[0].push(
  ["A", "B"],
  ["B", "D"],
  ["D", "E"],
  ["E", "F"],
  ["B", "C"],
  ["C", "F"]
);
nodes[1] = "B";
graphs[1] = [];
graphs[1].push(
  ["A", "B"],
  ["B", "D"],
  ["D", "E"],
  ["E", "F"],
  ["B", "C"],
  ["C", "F"]
);
nodes[2] = "C";
graphs[2] = [];
graphs[2].push(
  ["A", "B"],
  ["B", "D"],
  ["D", "E"],
  ["E", "F"],
  ["B", "C"],
  ["C", "F"]
);
nodes[3] = "E";
graphs[3] = [];
graphs[3].push(
  ["A", "B"],
  ["B", "D"],
  ["D", "E"],
  ["E", "F"],
  ["B", "C"],
  ["C", "F"]
);

nodes[4] = "U";
graphs[4] = [];

nodes[4] = "U";
graphs[5] = [["A", "B"]];

nodes[6] = "B";
graphs[6] = [];
graphs[6].push(
  ["A", "B"],
  ["B", "D"],
  ["B", "R"],
  ["D", "E"],
  ["E", "F"],
  ["B", "C"],
  ["U", "V"],
  ["U", "F"],
  ["R", "U"],
  ["C", "R"]
);

let times = graphs.length;
for (let i = 0; i < times; i++)
  console.log(biggestSubGraph(graphs[i], nodes[i]));
