#include "lists.h"

/**
 * check_cycle - checks is linked list have
 *		a cycle in it or not
 * @head: the head of the linked list
 *
 * Return: 1 if the linked list have a cycle.
 *	0 otherwise
 */

int check_cycle(listint_t *head)
{
	listint_t *slowPtr, *fastPtr;

	slowPtr = head;
	fastPtr = head;

	while (slowPtr && fastPtr)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;

		if (slowPtr == fastPtr)
			return (1);
	}
	return (0);
}
