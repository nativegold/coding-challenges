from enum import Enum


STORAGE_OUTSIDE = "OUTSIDE"
STORAGE_BLANK = "BLANK"


class DeliveryMethod(Enum):
    FORK_LIFT = 0,
    CRANE = 1


def pop_container_with_crane(storage_list, container_location_dict, container_type):
    if container_type not in container_location_dict:
        return

    containers = []
    storage_row_len = len(storage_list[0])
    storage_col_len = len(storage_list)

    for i, j in container_location_dict[container_type]:
        storage_list[i][j] = STORAGE_BLANK
        containers.append((i, j))

    stack = []
    for container in containers:
        stack.append(container)

        while stack:
            i, j = stack.pop()

            if container_type in container_location_dict and (i, j) in container_location_dict[container_type]:
                container_location_dict[container_type].remove((i, j))

            if not (i - 1 < 0
                    or i + 1 >= storage_col_len
                    or j - 1 < 0
                    or j + 1 >= storage_row_len
                    or storage_list[i - 1][j] == STORAGE_OUTSIDE
                    or storage_list[i + 1][j] == STORAGE_OUTSIDE
                    or storage_list[i][j - 1] == STORAGE_OUTSIDE
                    or storage_list[i][j + 1] == STORAGE_OUTSIDE):
                continue

            storage_list[i][j] = STORAGE_OUTSIDE

            if i - 1 >= 0 and storage_list[i - 1][j] == STORAGE_BLANK:
                stack.append((i - 1, j))

            if i + 1 < storage_col_len and storage_list[i + 1][j] == STORAGE_BLANK:
                stack.append((i + 1, j))

            if j - 1 >= 0 and storage_list[i][j - 1] == STORAGE_BLANK:
                stack.append((i, j - 1))

            if j + 1 < storage_row_len and storage_list[i][j + 1] == STORAGE_BLANK:
                stack.append((i, j + 1))


def pop_container_with_fork_lift(storage_list, container_location_dict, container_type):
    if container_type not in container_location_dict:
        return

    containers = []
    storage_row_len = len(storage_list[0])
    storage_col_len = len(storage_list)

    for i, j in container_location_dict[container_type]:
        if not (i - 1 < 0
                or i + 1 >= storage_col_len
                or j - 1 < 0
                or j + 1 >= storage_row_len
                or storage_list[i - 1][j] == STORAGE_OUTSIDE
                or storage_list[i + 1][j] == STORAGE_OUTSIDE
                or storage_list[i][j - 1] == STORAGE_OUTSIDE
                or storage_list[i][j + 1] == STORAGE_OUTSIDE):
            continue

        containers.append((i, j))

    stack = []
    for container in containers:
        stack.append(container)

        while stack:
            i, j = stack.pop()

            storage_list[i][j] = STORAGE_OUTSIDE

            if container_type in container_location_dict and (i, j) in container_location_dict[container_type]:
                container_location_dict[container_type].remove((i, j))

            if i - 1 >= 0 and storage_list[i - 1][j] == STORAGE_BLANK:
                stack.append((i - 1, j))

            if i + 1 < storage_col_len and storage_list[i + 1][j] == STORAGE_BLANK:
                stack.append((i + 1, j))

            if j - 1 >= 0 and storage_list[i][j - 1] == STORAGE_BLANK:
                stack.append((i, j - 1))

            if j + 1 < storage_row_len and storage_list[i][j + 1] == STORAGE_BLANK:
                stack.append((i, j + 1))


def deliver(storage_list, container_location_dict, container_type, delivery_method):
    if container_type not in container_location_dict:
        return

    if delivery_method == DeliveryMethod.CRANE:
        pop_container_with_crane(storage_list, container_location_dict, container_type)
    elif delivery_method == DeliveryMethod.FORK_LIFT:
        pop_container_with_fork_lift(storage_list, container_location_dict, container_type)


def solution(storage, requests):
    answer = 0
    storage_list = [list(s) for s in storage]
    container_location_dict = {}

    for i in range(len(storage_list)):
        for j in range(len(storage_list[0])):
            if storage_list[i][j] not in container_location_dict:
                container_location_dict[storage_list[i][j]] = set()
            container_location_dict[storage_list[i][j]].add((i, j))

    for request in requests:
        container_type = request[0]

        if container_type not in container_location_dict:
            continue

        delivery_method = DeliveryMethod.CRANE if len(request) > 1 else DeliveryMethod.FORK_LIFT
        deliver(storage_list, container_location_dict, container_type, delivery_method)

    for container_location_set in container_location_dict.values():
        answer += len(container_location_set)

    return answer