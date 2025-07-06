#include "lists.h"

/**
 * check_cycle - function checks is a singly linked list has a cycle in it
 * @list: the head of the singly linked list to check
 * Return: 1 is the list has a cycle in it, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fastPtr;
	listint_t *slowPtr;
	
	if (!list || !list->next)
		return (0);

	slowPtr = list;
	fastPtr = list->next;

	while (fastPtr->next)
	{
		if (fastPtr == slowPtr)
			return (1);
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
	}
	return (0);
}
