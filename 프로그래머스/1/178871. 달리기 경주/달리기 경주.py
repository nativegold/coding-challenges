def solution(players, callings):
    result = list(players)
    current_ranking = {}
    
    ranking = 1
    for player in players:
        current_ranking[player] = ranking
        ranking += 1
    
    for calling in callings:
        old_ranking_player = result[current_ranking[calling] - 2]
        new_ranking_player = result[current_ranking[calling] - 1]
        result[current_ranking[calling] - 2], result[current_ranking[calling] - 1] = new_ranking_player, old_ranking_player

        current_ranking[new_ranking_player] -= 1
        current_ranking[old_ranking_player] += 1
    
    return result