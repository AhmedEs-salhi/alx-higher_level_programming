#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that adds a node into a sorted singly linked list
 * @list: the head of the singly linked list
 * @number: the number of the new node
 * Return: returns the new added node, or NULL otherwise
 */
listint_t *insert_node(listint_t **list, int number)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	new->n = number;
	if (!(*list))
	{
		*list = new;
		new->next = NULL;
	}
	prev = *list;
	curr = prev->next;
	if (prev->n > number)
	{
		new->next = *list;
		*list = new;
		return (new);
	}
	else if ((prev->n < number) && !curr)
	{
		prev->next = new;
		new->next = curr;
		return (new);
	}
	while (prev->next)
	{
		if (curr->n > number)
		{
			prev->next = new;
			new->next = curr;
			return (new);
		}
		prev = curr;
		curr = curr->next;
	}
	prev->next = new;
	new->next = NULL;
	return (new);
}
