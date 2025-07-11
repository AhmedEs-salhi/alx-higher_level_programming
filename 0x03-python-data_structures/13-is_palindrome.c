#include <stdlib.h>
#include "lists.h"

/**
 * list_length - gives the length of a singly linked list
 *
 * @head: the head of the singly linked list
 * Return: the size of the singly linked list, 0 otherwise
 */
int list_length(listint_t **head)
{
	listint_t *current;
	int length;

	if (!(*head))
		return (0);

	current = *head;
	length = 0;
	while (current)
	{
		current = current->next;
		length++;
	}
	return (length);
}

/**
 * is_even - checks if a number is even or not
 *
 * @number: the number to be checked
 * Return: 1 if the number is even, 0 otherwise
 */
int is_even(int number)
{
	return (!(number % 2));
}

/**
 * is_palindrome - checks if a singly linked list is palindrome
 *
 * @head: the head of the singly linked list
 * Return: 1 if the singly linked list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int first_half_array[500];
	listint_t *node_current_pointer;
	int list_length_variable;
	size_t first_half_array_size;
	int helper_variable;
	int array_index;


	if (!(*head))
		return (1);

	list_length_variable = list_length(head);
	first_half_array_size = list_length_variable / 2;


	array_index = first_half_array_size - 1;
	helper_variable = 1;
	node_current_pointer = *(head);
	while ((size_t)helper_variable <= first_half_array_size)
	{
		first_half_array[array_index--] = node_current_pointer->n;
		node_current_pointer = node_current_pointer->next;
		helper_variable++;
	}
	if (!is_even(list_length_variable))
		node_current_pointer = node_current_pointer->next;

	array_index = 0;
	while (node_current_pointer)
	{
		if (first_half_array[array_index++] != node_current_pointer->n)
			return (0);
		node_current_pointer = node_current_pointer->next;
	}
	return (1);
}
