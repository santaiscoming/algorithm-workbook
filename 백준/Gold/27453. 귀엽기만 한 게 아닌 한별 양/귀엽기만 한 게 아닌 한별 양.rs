use std::collections::VecDeque;
use std::io::{self, Read};
use std::fs::File;

// 격자의 각 칸 상태를 정의하는 Enum
#[derive(Clone, Copy, PartialEq, Debug)]
enum Tile {
    Wall,      // X
    Start,     // S
    Home,      // H
    Cost(i32), // 0-9 (불운도)
}

fn main() {
    // ------------------------------------------------------------------
    // sys.stdin = open("input.txt", "r") # ❌ 대응 구문
    // 로컬에 "input.txt" 파일이 있으면 읽고, 없으면 표준 입력(stdin)을 사용합니다.
    // ------------------------------------------------------------------
    let mut buffer = String::new();
    if let Ok(mut f) = File::open("input.txt") {
        f.read_to_string(&mut buffer).unwrap();
    } else {
        io::stdin().read_to_string(&mut buffer).unwrap();
    }
    // ------------------------------------------------------------------

    // 입력을 공백/줄바꿈 기준으로 분리하여 처리 (Fast I/O)
    let mut iter = buffer.split_whitespace();

    // N(세로), M(가로), K(불운도 제한) 파싱
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();
    let k: i32 = iter.next().unwrap().parse().unwrap();

    let mut village = Vec::with_capacity(n);
    let mut start_pos = None;

    // 격자 데이터 파싱
    for y in 0..n {
        let row_str = iter.next().unwrap();
        let mut row = Vec::with_capacity(m);
        for (x, c) in row_str.chars().enumerate() {
            let tile = match c {
                'S' => {
                    start_pos = Some((x, y));
                    Tile::Start
                },
                'H' => Tile::Home,
                'X' => Tile::Wall,
                d if d.is_digit(10) => Tile::Cost(d.to_digit(10).unwrap() as i32),
                _ => Tile::Wall, // 예외 처리
            };
            row.push(tile);
        }
        village.push(row);
    }

    if start_pos.is_none() {
        println!("-1");
        return;
    }

    let (sx, sy) = start_pos.unwrap();

    // 방향: (dx, dy) - Python 코드 순서: (1, 0), (0, 1), (-1, 0), (0, -1)
    let directions = [(1, 0), (0, 1), (-1, 0), (0, -1)];

    // 방문 체크: visited[y][x][direction_index]
    // 3차원 배열: N x M x 4
    let mut visited = vec![vec![[false; 4]; m]; n];

    // 큐: (x, y, px, py, cost)
    let mut q = VecDeque::new();
    // Python 로직 반영: 시작점의 px, py는 (0,0)으로 초기화
    q.push_back((sx, sy, 0, 0, 0));

    while let Some((x, y, px, py, cost)) = q.pop_front() {
        for (i, &(dx, dy)) in directions.iter().enumerate() {
            let nx = x as isize + dx;
            let ny = y as isize + dy;

            // 1. 범위 체크
            if nx < 0 || nx >= m as isize || ny < 0 || ny >= n as isize {
                continue;
            }

            let nx = nx as usize;
            let ny = ny as usize;

            // 2. 벽('X'), 출발지('S'), 바로 직전 위치(Backtrack 방지) 체크
            match village[ny][nx] {
                Tile::Wall => continue,
                Tile::Start => continue,
                _ => {}
            }
            if (nx, ny) == (px, py) {
                continue;
            }

            // 3. 목적지('H') 도착 체크
            if let Tile::Home = village[ny][nx] {
                println!("{}", cost + 1);
                return;
            }

            // 4. 불운도 합계 계산 (Prev + Curr + Next)
            // prevUnlucky
            let prev_unlucky = match village[py][px] {
                Tile::Cost(val) => val,
                _ => 0, // 'S', 'H' 등은 0 처리 (Python 로직 반영)
            };

            // currUnlucky
            let curr_unlucky = match village[y][x] {
                Tile::Start => 0,
                Tile::Cost(val) => val,
                _ => 0,
            };

            // nextUnlucky
            let next_unlucky = match village[ny][nx] {
                Tile::Cost(val) => val,
                _ => 0, // 'H'는 위에서 처리됨
            };

            if prev_unlucky + curr_unlucky + next_unlucky > k {
                continue;
            }

            // 5. 방문 체크 및 큐 삽입
            if !visited[ny][nx][i] {
                visited[ny][nx][i] = true;
                q.push_back((nx, ny, x, y, cost + 1));
            }
        }
    }

    // 도달 불가능 시
    println!("-1");
}